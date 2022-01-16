FROM golang:latest AS go_build
WORKDIR /go
COPY app.go .

RUN CGO_ENABLED=0 go build -o mybin app.go
RUN ls

FROM alpine:latest
EXPOSE 5002
COPY --from=go_build /go/mybin /usr/local/bin/mybin
RUN chmod +x /usr/local/bin/mybin

CMD ["/usr/local/bin/mybin"]
