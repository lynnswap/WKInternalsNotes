# ``WKInternalsNotes/WKQuickboardViewControllerDelegate/inputLabelTextForViewController(_:)``

入力ラベルの文言を返す。

## Objective-C Declaration
```objective-c
- (NSString *)inputLabelTextForViewController:(PUICQuickboardViewController *)controller;
```

## Discussion
`WKContentViewInteraction` の実装では `inputLabelText` をそのまま返す。

## References
- [`WKQuickboardViewControllerDelegate.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKQuickboardViewControllerDelegate.h#L32)
- [`WKContentViewInteraction.mm#L12043`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12043)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
