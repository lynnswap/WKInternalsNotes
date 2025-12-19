# ``WKInternalsNotes/WKTextExtractionSelectItem/initWithSelectedValues(_:supportsMultiple:rectInWebView:children:eventListeners:ariaAttributes:accessibilityRole:nodeIdentifier:)``

選択項目の情報を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithSelectedValues:(NSArray<NSString *> *)selectedValues supportsMultiple:(BOOL)supportsMultiple rectInWebView:(CGRect)rectInWebView children:(NSArray<WKTextExtractionItem *> *)children eventListeners:(WKTextExtractionEventListenerTypes)eventListeners ariaAttributes:(NSDictionary<NSString *, NSString *> *)ariaAttributes accessibilityRole:(NSString *)accessibilityRole nodeIdentifier:(nullable NSString *)nodeIdentifier;
```

## Discussion
`selectedValues` と `supportsMultiple` を保持し、`WKTextExtractionItem` の `init(with:)` に共通項目を渡して初期化する。

## References
- [`_WKTextExtractionInternal.h#L167`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L167)
- [`_WKTextExtraction.swift#L395`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L395)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
