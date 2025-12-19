# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/initWithEditable(_:controlType:autocomplete:isReadonly:isDisabled:isChecked:rectInWebView:children:eventListeners:ariaAttributes:accessibilityRole:nodeIdentifier:)``

テキストフォームコントロールの情報を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithEditable:(WKTextExtractionEditable *)editable controlType:(NSString *)controlType autocomplete:(NSString *)autocomplete isReadonly:(BOOL)isReadonly isDisabled:(BOOL)isDisabled isChecked:(BOOL)isChecked rectInWebView:(CGRect)rectInWebView children:(NSArray<WKTextExtractionItem *> *)children eventListeners:(WKTextExtractionEventListenerTypes)eventListeners ariaAttributes:(NSDictionary<NSString *, NSString *> *)ariaAttributes accessibilityRole:(NSString *)accessibilityRole nodeIdentifier:(nullable NSString *)nodeIdentifier;
```

## Discussion
`editable` や各種フラグを保持し、`WKTextExtractionItem` の `init(with:)` に共通項目を渡して初期化する。

## References
- [`_WKTextExtractionInternal.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L141)
- [`_WKTextExtraction.swift#L190`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L190)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
