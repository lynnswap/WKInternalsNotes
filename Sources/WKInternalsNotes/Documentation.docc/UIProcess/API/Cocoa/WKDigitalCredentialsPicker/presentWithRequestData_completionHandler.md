# ``WKInternalsNotes/WKDigitalCredentialsPicker/presentWithRequestData(_:completionHandler:)``

デジタルクレデンシャル要求を提示し、完了時に結果を返す。

## Objective-C Declaration
```objective-c
- (void)presentWithRequestData:(const WebCore::DigitalCredentialsRequestData&)requestData completionHandler:(CompletionHandler<void(Expected<WebCore::DigitalCredentialsResponseData, WebCore::ExceptionData>&&)>&&)completionHandler;
```

## Discussion
`completionHandler` を保存し、`_presentmentController` を準備してから `performRequest:` を実行する。提示後、`delegate` が `digitalCredentialsPickerDidPresent:` を実装していれば通知する。

## References
- [`WKDigitalCredentialsPicker.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/DigitalCredentials/WKDigitalCredentialsPicker.h#L64)
- [`WKDigitalCredentialsPicker.mm#L271`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/DigitalCredentials/WKDigitalCredentialsPicker.mm#L271)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
