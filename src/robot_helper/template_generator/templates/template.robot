*** Settings ***
Documentation     {% for line in suite_doc %}
{{ line }}
{% endfor %}
Resource          ./base.robot


*** Variables ***


*** Test Cases ***
{{cvt_case_name}}
    [Documentation]    {% for line in case_doc %}
{{ line }}
{% endfor %}
    [Tags]       @author={{form.author_name.data}}     @TCID={{form.tcid.data}}
    [Setup]      {{ case_setup_name }}
    [Teardown]   {{ case_teardown_name }}
{% for line in log_lines %}
    {{ line }}

{% endfor %}


*** Keywords ***
{{ case_setup_name }}
    [Documentation]
    [Arguments]


{{ case_teardown_name }}
    [Documentation]
    [Arguments]