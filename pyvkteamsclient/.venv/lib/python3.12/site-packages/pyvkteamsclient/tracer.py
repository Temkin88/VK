from opentelemetry.trace import get_tracer

tracer = get_tracer(instrumenting_module_name=__name__)
