FROM golang:latest AS builder

WORKDIR /app
COPY go_server.go ./
COPY flag.txt ./

RUN CGO_ENABLED=0 GOOS=linux go build go_server.go

FROM alpine:latest

WORKDIR /app

COPY --from=builder /app/go_server /app/go_server
COPY --from=builder /app/flag.txt .

EXPOSE 8080

CMD ["/app/go_server"]

