# ``WKInternalsNotes/WKWebView/_intelligenceBaseClass``

UIIntelligence 連携用の基底クラスを返す。

## Swift Declaration
```swift
open override var _intelligenceBaseClass: AnyClass
```

## Default Value
`WKWebView.self` を返す。

## Discussion
UIIntelligence の基底クラスとして `WKWebView.self` を返す override 実装。

## References
- [WKWebView+TextExtraction.swift#L87](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/TextExtraction/WKWebView+TextExtraction.swift#L87)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
