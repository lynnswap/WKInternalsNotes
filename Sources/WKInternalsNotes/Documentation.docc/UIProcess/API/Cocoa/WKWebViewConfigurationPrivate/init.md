# ``WKInternalsNotes/WKWebViewConfiguration/init(_:)``

`WebPage.Configuration` から `WKWebViewConfiguration` を構築する。

## Swift Declaration
```swift
convenience init(_ wrapped: WebPage.Configuration)
```

## Discussion
ラップされた `WebPage.Configuration` の各値を `WKWebViewConfiguration` に転写し、既定の `WKWebpagePreferences` や URL スキームハンドラも設定する。

## References
- [WKWebViewConfiguration+Extras.swift#L30](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration+Extras.swift#L30)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
