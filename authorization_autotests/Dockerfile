FROM registry-gitlab.corp.mail.ru/mail-admins/images/system/almalinux9:9.5-20250227-0

ENV PIP_INDEX_URL="https://oneart.vkteam.ru/repository/pypi/simple/"
ENV PIP_EXTRA_INDEX_URL="https://__token__:9sB-zvU818WmFwkXechX@gitlab.corp.mail.ru/api/v4/groups/3011/-/packages/pypi/simple"
ENV PIP_TRUSTED_HOST="oneart.vkteam.ru gitlab.corp.mail.ru"

COPY pyproject.toml /app/pyproject.toml
COPY tests/__init__.py /app/tests/__init__.py
WORKDIR /app
 #  hadolint ignore=DL3009,DL3015
RUN dnf -y update && \
    rm -vf /etc/yum.repos.d/almalinux* && \
    dnf install python3.14-3.14.4-2.el9_8 -y && \
    dnf install -y \
      python3.14-pip-wheel-25.2-3.el9.noarch \
      python3.14-devel-3.14.4-2.el9_8.x86_64 \
      krb5-devel-1.21.1-10.el9_8.x86_64 \
      gcc-11.5.0-14.el9.alma.1.x86_64  && \
    dnf clean all && \
    python3.14 -m venv .venv

ENV PATH="/app/.venv/bin:$PATH"
RUN python3 -m pip install --no-cache-dir --upgrade pip==26.0.1 && \
    python3 -m pip install --no-cache-dir .

COPY .  .

CMD [ "/bin/sleep", "infinity" ]