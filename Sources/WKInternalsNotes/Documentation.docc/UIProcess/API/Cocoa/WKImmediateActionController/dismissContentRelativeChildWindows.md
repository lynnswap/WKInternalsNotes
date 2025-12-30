# ``WKInternalsNotes/WKImmediateActionController/dismissContentRelativeChildWindows()``

関連する子ウィンドウを閉じる。

## Objective-C Declaration
```objective-c
- (void)dismissContentRelativeChildWindows;
```

## Discussion
`setMaintainsInactiveSelection(false)` を呼び、現在の Quick Look メニュー項目を閉じる。

## References
- [`WKImmediateActionController.h#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKImmediateActionController.h#L83)
- [`WKImmediateActionController.mm#L151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKImmediateActionController.mm#L151)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
