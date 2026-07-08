'use strict'

class BridgeError extends Error {
  constructor(code, reason) {
    super(`${code}: ${reason}`)
    this.code = code
    this.reason = reason
  }
}

let promises = {}

let functionCall = (name) => (...args) => {
  let reqId = Math.random().toString(36).substr(2)

  window.parent.postMessage(
    {
      type: "functionCall",
      data: {
        reqId: reqId,
        name: name,
        args: args,
      },
    },
    '*'
  )

  return new Promise((resolve, reject) => {
    promises[reqId] = [resolve, reject]
  })
}

let subscriptions = {}

let callBackHandlers = {
  newEvent: (subscriptionId, eventAttributes) => {
    let callback = subscriptions[subscriptionId]
    if (!callback) {
      throw new BridgeError('SUBSCRIPTION_NOT_FOUND', `no subscription found with id ${subscriptionId}`)
    }
    callback(eventAttributes)
  }
}

window.addEventListener(
  "message",
  event => {
    if (typeof event.data !== 'object') {
      return
    }
    switch (event.data.type) {
    case 'functionCallReply':
      let replyData = event.data.data
      let promise = promises[replyData.reqId]
      if (promise) {
        delete promises[replyData.reqId]

        let [resolve, reject] = promise

        if (replyData.ok !== undefined) {
          resolve(replyData.ok)
        } else {
          console.warn(`rejecting req ${replyData.reqId} promise: ${replyData.err}`)
          reject(replyData.err)
        }
      } else {
        console.warn(`got reply to unknown function call with id ${replyData.reqId}`)
      }
      break
    case 'callBack':
      let requestData = event.data.data
      let callBackReply = ({ ok, err }) => {
        if ((ok === undefined) === (err === undefined)) {
          return callBackReply({
            err: {
              code: 'INTERNAL_ERROR',
              reason: 'callBack handler protocol violation',
            }
          })
        }
        event.source.postMessage({
          type: "callBackReply",
          data: {
            reqId: requestData.reqId,
            ok,
            err,
          },
        }, event.origin)
      }
      let callback = callBackHandlers[requestData.name]
      if (!callback) {
        console.warn(`got callBack request with unknown name "${requestData.name}"`)
      }
      try {
        return callBackReply({
          ok: callback(...requestData.args) || null
        })
      } catch (e) {
        if (e instanceof BridgeError) {
          return callBackReply({
            err: {
              code: e.code,
              reason: e.reason,
            }
          })
        }
        if (e instanceof Error) {
          return callBackReply({
            err: {
              code: 'INTERNAL_ERROR',
              reason: `callBack handler raised an exception "${e.name}": "${e.message}"`,
            }
          })
        }
        return callBackReply({
          err: {
            code: 'INTERNAL_ERROR',
            reason: 'callBack handler raised an exception',
          }
        })
      }
      break
    }
  }
)

module.exports = Object.freeze({
  send: functionCall('send'),
  subscribe: (subscriptionName, callback, subscriptionParams) => {
    return functionCall('subscribe')(
      subscriptionName,
      subscriptionParams
    ).then(({
      subscriptionId
    }) => {
      subscriptions[subscriptionId] = callback
    })
  }
})




send(
    "LoadingCompleted", // string
    {
        ok: true
    }
)