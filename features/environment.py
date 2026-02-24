from Utils.Logger import setUP_Logger

def before_all(context):
    context.logger = setUP_Logger()
    context.logger.info('==================Test Execution Started=================')

def before_scenario(context, scenario):
    context.logger.info(f'==================Starting Scenario: {scenario.name}=================')

def after_scenario(context, scenario):
    context.logger.info(f'==================Ending Scenario: {scenario.name}=================')

def after_step(context, step):
    if step.status == 'failed':
        context.logger.error(f'Step failed: {step.name}')
    else:
        context.logger.info(f'Step passed: {step.name}')

def after_feature(context, feature):
    context.logger.info(f'==================Ending Feature: {feature.name}=================')

def after_tag(context, tag):
    context.logger.info(f'==================Ending Tag: {tag}=================')

def after_all(context):
    context.logger.info('==================Test Execution Completed=================')