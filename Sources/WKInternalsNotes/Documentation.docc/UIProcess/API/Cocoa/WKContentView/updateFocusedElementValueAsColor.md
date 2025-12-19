# ``WKInternalsNotes/WKContentView/updateFocusedElementValueAsColor(_:)``

フォーカス中要素の色値を更新する。

## Objective-C Declaration
```objective-c
- (void)updateFocusedElementValueAsColor:(UIColor *)value;
```

## Discussion
入力値を `WebCore::Color` に変換し、HTML 文字列へシリアライズして `_page->setFocusedElementValue` に渡す。`_focusedElementInformation.value` と `colorValue` を更新する。

## References
- [`WKContentViewInteraction.h#L874`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L874)
- [`WKContentViewInteraction.mm#L6240`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6240)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
