# ``WKInternalsNotes/WKWebView/_intelligenceCollectRemoteContent(in:remoteContextWrapper:)``

可視領域のテキスト抽出結果を UIIntelligence に送る。

## Swift Declaration
```swift
open override func _intelligenceCollectRemoteContent(in visibleRect: CGRect, remoteContextWrapper: UIIntelligenceCollectionRemoteContextWrapper)
```

## Discussion
MainActor の Task 内で `_WKTextExtractionConfiguration` を組み立て、`_requestTextExtraction` の結果を `collector.collect` で送信する。

## References
- [WKWebView+TextExtraction.swift#L102](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/TextExtraction/WKWebView+TextExtraction.swift#L102)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
