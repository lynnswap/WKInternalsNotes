# ``WKInternalsNotes/WKDigitalCredentialsPicker/initWithView(_:page:)``

`WKWebView` と `WebPageProxy` を保持する初期化子。

## Objective-C Declaration
```objective-c
- (instancetype)initWithView:(WKWebView *)view page:(WebKit::WebPageProxy*)page;
```

## Discussion
`[super init]` に成功した場合、`_webView` と `_page` を保存して初期化を完了する。

## References
- [`WKDigitalCredentialsPicker.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/DigitalCredentials/WKDigitalCredentialsPicker.h#L62)
- [`WKDigitalCredentialsPicker.mm#L212`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/DigitalCredentials/WKDigitalCredentialsPicker.mm#L212)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
