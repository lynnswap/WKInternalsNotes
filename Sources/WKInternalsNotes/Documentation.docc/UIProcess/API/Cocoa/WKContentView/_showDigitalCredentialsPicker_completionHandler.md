# ``WKInternalsNotes/WKContentView/_showDigitalCredentialsPicker(_:completionHandler:)``

デジタルクレデンシャルのピッカーを表示する。

## Objective-C Declaration
```objective-c
- (void)_showDigitalCredentialsPicker:(const WebCore::DigitalCredentialsRequestData&)requestData completionHandler:(WTF::CompletionHandler<void(Expected<WebCore::DigitalCredentialsResponseData, WebCore::ExceptionData>&&)>&&)completionHandler;
```

## Discussion
`WKDigitalCredentialsPicker` を生成し、WebView と `WebPageProxy` を渡して `presentWithRequestData:completionHandler:` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L834`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L834)
- [`WKContentViewInteraction.mm#L9765`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9765)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
