# syntax=docker/dockerfile:1.7
FROM python:3.12-slim AS builder

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

RUN python -m venv "${VIRTUAL_ENV}" \
    && pip install --no-cache-dir --upgrade pip build

WORKDIR /build
COPY pyproject.toml README.md ./
COPY src ./src
RUN --mount=type=bind,source=.git,target=/build/.git,readonly \
    python -m build --wheel \
    && pip install --no-cache-dir dist/magi-*.whl

FROM python:3.12-slim AS final

ARG UID=13337
ARG USER=runner
RUN useradd --uid "${UID}" --create-home "${USER}"

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

COPY --from=builder "${VIRTUAL_ENV}" "${VIRTUAL_ENV}"
USER ${UID}:${UID}

ENTRYPOINT ["magi"]
CMD ["--help"]
