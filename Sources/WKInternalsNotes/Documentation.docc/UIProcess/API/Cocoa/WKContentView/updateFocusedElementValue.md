# ``WKInternalsNotes/WKContentView/updateFocusedElementValue(_:)``

フォーカス中要素の値を更新する。

## Objective-C Declaration
```objective-c
- (void)updateFocusedElementValue:(NSString *)value;
```

## Discussion
`_page->setFocusedElementValue` に値を渡し、`_focusedElementInformation.value` を更新する。

## References
- [`WKContentViewInteraction.h#L875`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L875)
- [`WKContentViewInteraction.mm#L6234`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6234)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
