FROM gradle:6.0.1-jdk8

ENV SDK_URL="https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip"
ENV ANDROID_HOME="/usr/local/android-sdk"
ENV ANDROID_VERSION=29
ENV ANDROID_BUILD_TOOLS_VERSION=27.0.3

ARG DEBIAN_FRONTEND=noninteractive

# Download Android SDK
RUN mkdir "$ANDROID_HOME" ~/.android && touch ~/.android/repositories.cfg && \
    cd "$ANDROID_HOME" && \
    curl -o sdk.zip $SDK_URL && \
    unzip -q sdk.zip && \
    rm sdk.zip

ENV PATH ${ANDROID_HOME}/tools/bin:$ANDROID_HOME/platform-tools:$PATH

# Accept License
RUN yes | sdkmanager --licenses

# Install Android Build Tool and Libraries
RUN sdkmanager --update

RUN sdkmanager "build-tools;${ANDROID_BUILD_TOOLS_VERSION}" \
    "platforms;android-${ANDROID_VERSION}" \
    "platform-tools"

# Install Build Essentials
RUN apt-get update && \
    apt-get install -y build-essential file apt-utils tzdata wget vim unzip zip curl && \
    rm -rf /var/cache/apk/*

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /workspace