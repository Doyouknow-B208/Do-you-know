FROM openjdk:8 AS builder
COPY gradlew .
COPY gradle gradle
COPY build.gradle .
COPY settings.gradle .
COPY src src
RUN chmod =x ./gradlew
RUN ./gradlew bootJar
#RUN ./gradlew clean build --exclude-task test

FROM openjdk:8
COPY --from=builder build/libs/DoYouKnow-0.0.1-SNAPSHOT.jar DoYouKnow.jar

EXPOSE 8080
CMD ["java","-jar","/DoYouKnow.jar"]