# ``WKInternalsNotes/WKTextExtractionTextItem/initWithContent(_:selectedRange:links:editable:rectInWebView:children:eventListeners:ariaAttributes:accessibilityRole:nodeIdentifier:)``

テキスト項目の情報を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithContent:(NSString *)content selectedRange:(NSRange)selectedRange links:(NSArray<WKTextExtractionLink *> *)links editable:(WKTextExtractionEditable * _Nullable)editable rectInWebView:(CGRect)rectInWebView children:(NSArray<WKTextExtractionItem *> *)children eventListeners:(WKTextExtractionEventListenerTypes)eventListeners ariaAttributes:(NSDictionary<NSString *, NSString *> *)ariaAttributes accessibilityRole:(NSString *)accessibilityRole nodeIdentifier:(nullable NSString *)nodeIdentifier;
```

## Discussion
`content` / `selectedRange` / `links` / `editable` を保持し、`WKTextExtractionItem` の `init(with:)` に共通項目を渡して初期化する。

## References
- [`_WKTextExtractionInternal.h#L154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L154)
- [`_WKTextExtraction.swift#L324`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L324)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
