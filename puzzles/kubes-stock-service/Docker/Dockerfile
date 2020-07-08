FROM golang:1.14

WORKDIR /go/src/app
COPY ./stock.go .

RUN go build stock.go

EXPOSE 8080/tcp

CMD ["./stock"]
