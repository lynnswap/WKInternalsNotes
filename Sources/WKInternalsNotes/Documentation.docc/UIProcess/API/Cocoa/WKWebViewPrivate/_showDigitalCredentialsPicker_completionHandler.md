# ``WKInternalsNotes/WKWebView/_showDigitalCredentialsPicker(_:completionHandler:)``

`_showDigitalCredentialsPicker` を表示する。

## Objective-C Declaration
```objective-c
- (void)_showDigitalCredentialsPicker:(const WebCore::DigitalCredentialsRequestData&)requestData completionHandler:(WTF::CompletionHandler<void(Expected<WebCore::DigitalCredentialsResponseData, WebCore::ExceptionData>&&)>&&)completionHandler;
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewInternal.h#L569`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L569)
- [`API/Cocoa/WKWebView.mm#L342`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L342)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
