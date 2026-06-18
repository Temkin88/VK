UserQuery = {
    "operationName": "UserQuery",
    "variables": {},
    "query": """query UserQuery {
      user {
          email
          name
          workingDays
          workingTime {
          from
          to
          __typename
          }
          timezone {
          name
          offset
          regionID
          __typename
          }
          tutorial
          __typename
      }
  }""",
}

CreateCalendarUser = {
    "operationName": "CreateUser",
    "variables": {},
    "query": """mutation CreateUser {
      createUser {
        email
        name
        workingDays
        workingTime {
            from
            to
            __typename
        }
        timezone {
            name
            offset
            __typename
        }
        tutorial
        __typename
      }
  }""",
}


CreateEvent = {
    "query": """mutation CreateEvent($input: EventInput!) {
      createEvent(event: $input) {
        uid
        title
        from
        to
        fullDay
        description
        recurrenceID
        calendar {
          uid
          __typename
        }
        reminders {
          interval
          type
          __typename
        }
        attaches {
          url
          shareID
          filename
          size
          __typename
        }
        call
        location {
          description
        }
        recurrence {
          freq
          weekdays {
            day
            __typename
          }
          monthdays
          interval
          exdates
          __typename
        }
        note {
          uid
          __typename
        }
        attendeesCanInvite
        __typename
      }
    }""",
    "variables": {},
}

CreateCalendar = {
    "query": """mutation CreateCalendar($input: CalendarInput!) {
        createCalendar(calendar: $input) {
            uid
            title
            type
            color
            attendees {
                user {
                    email
                    name
                    __typename
                }
                __typename
            }
            __typename
        }
    }""",
    "variables": {},
}

GetSingleEvent = {
    "query": """query FetchEvent(
        $eventUID: UID!,
        $calendarUID: UID!,
        $recurrentID: Time
    ) {
        event(eventUID: $eventUID, calendarUID: $calendarUID, recurrentID: $recurrentID) {
            uid
            title
            from
            to
            fullDay
            recurrenceID
            status
            call
            color
            description
            calendar {
                uid
                color
                isMLCostil
                type
                title
                owner {
                    email
                    name
                    __typename
                }
                __typename
            }
            call
            access
            isVirtual
            isOrganizer
            inviteMessageInfo {
                uidl
                folderID
                threadID
                from
                subject
                __typename
            }
            ... on Event {
                attaches {
                    url
                    shareID
                    filename
                    size
                    __typename
                }
                __typename
            }
            inviteMessageAttaches {
                path
                folderID
                name
                __typename
            }
            source
            customProps {
                specProject
                MLPhone
                MLData {
                    type
                    subtype
                    __typename
                }
                __typename
            }
            attendeesCanInvite
            ... on Event {
                location {
                    description
                    geo {
                        latitude
                        longitude
                        __typename
                    }
                    __typename
                }
                __typename
            }
            ... on Event {
                organizer {
                    email
                    name
                    role
                    status
                    __typename
                }
                __typename
            }
            ... on Event {
                suggestsEventTime {
                    from
                    to
                    author {
                        email
                        name
                        __typename
                    }
                    comment
                    __typename
                }
                __typename
            }
            __typename
        }
    }
    """,
    "variables": {},
}

CalendarsQuery = {
    "query": """query CalendarsQuery {
      calendars(onlyAccepted: false) {
        uid
        title
        status
        type
        access
        isMLCostil
        isDefault
        color
        sortWeight
        shareReminders
        receiveSharedReminders
        sharingToken {
          token
          access
          __typename
        }
        owner {
          email
          name
          __typename
        }
        attendees(inviteTypes: [DIRECT]) {
          user {
            name
            email
            __typename
          }
          access
          status
          __typename
        }
        reminders {
          type
          interval
          __typename
        }
        description
        freebusyEnabled
        sync {
          URL
          __typename
        }
        isUnsubscribable
        __typename
      }
    }""",
    "variables": {},
}
