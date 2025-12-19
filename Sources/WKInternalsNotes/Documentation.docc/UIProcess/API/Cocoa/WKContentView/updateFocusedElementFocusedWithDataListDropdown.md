# ``WKInternalsNotes/WKContentView/updateFocusedElementFocusedWithDataListDropdown(_:)``

datalist ドロップダウン表示中フラグを更新する。

## Objective-C Declaration
```objective-c
- (void)updateFocusedElementFocusedWithDataListDropdown:(BOOL)value;
```

## Discussion
`_focusedElementInformation.isFocusingWithDataListDropdown` を更新し、`reloadInputViews` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L877`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L877)
- [`WKContentViewInteraction.mm#L6259`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6259)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
