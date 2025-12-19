# ``WKInternalsNotes/WKWebView/_intelligenceCollectContent(in:collector:)``

UIIntelligence のリモートコンテキスト収集を開始する。

## Swift Declaration
```swift
open override func _intelligenceCollectContent(in visibleRect: CGRect, collector: UIIntelligenceElementCollector)
```

## Discussion
`collector.context.createRemoteContext` を生成し、`.remote` として収集対象に追加する。

## References
- [WKWebView+TextExtraction.swift#L92](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/TextExtraction/WKWebView+TextExtraction.swift#L92)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
