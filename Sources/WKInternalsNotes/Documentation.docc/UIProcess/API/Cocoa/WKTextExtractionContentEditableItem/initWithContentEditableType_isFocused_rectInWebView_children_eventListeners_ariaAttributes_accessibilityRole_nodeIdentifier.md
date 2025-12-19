# ``WKInternalsNotes/WKTextExtractionContentEditableItem/initWithContentEditableType(_:isFocused:rectInWebView:children:eventListeners:ariaAttributes:accessibilityRole:nodeIdentifier:)``

contenteditable 要素の情報を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithContentEditableType:(WKTextExtractionEditableType)contentEditableType isFocused:(BOOL)isFocused rectInWebView:(CGRect)rectInWebView children:(NSArray<WKTextExtractionItem *> *)children eventListeners:(WKTextExtractionEventListenerTypes)eventListeners ariaAttributes:(NSDictionary<NSString *, NSString *> *)ariaAttributes accessibilityRole:(NSString *)accessibilityRole nodeIdentifier:(nullable NSString *)nodeIdentifier;
```

## Discussion
Swift extension の `init` で `contentEditableType` と `isFocused` を保持し、`WKTextExtractionItem` の `init(with:)` に他の引数を渡して初期化する。

## References
- [`_WKTextExtractionInternal.h#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L135)
- [`_WKTextExtraction.swift#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L110)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
