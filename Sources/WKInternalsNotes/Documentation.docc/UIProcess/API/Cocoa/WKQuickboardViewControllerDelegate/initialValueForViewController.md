# ``WKInternalsNotes/WKQuickboardViewControllerDelegate/initialValueForViewController(_:)``

入力の初期値を返す。

## Objective-C Declaration
```objective-c
- (NSString *)initialValueForViewController:(PUICQuickboardViewController *)controller;
```

## Discussion
`WKContentViewInteraction` の実装では `_focusedElementInformation.value` を文字列として返す。

## References
- [`WKQuickboardViewControllerDelegate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKQuickboardViewControllerDelegate.h#L33)
- [`WKContentViewInteraction.mm#L12048`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12048)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
