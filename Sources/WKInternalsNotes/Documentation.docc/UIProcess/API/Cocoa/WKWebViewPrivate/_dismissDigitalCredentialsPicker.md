# ``WKInternalsNotes/WKWebView/_dismissDigitalCredentialsPicker(_:)``

`_dismissDigitalCredentialsPicker` を実行する。

## Objective-C Declaration
```objective-c
- (void)_dismissDigitalCredentialsPicker:(WTF::CompletionHandler<void(bool)>&&)completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewInternal.h#L570`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L570)
- [`WKWebView.mm#L348`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L348)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
