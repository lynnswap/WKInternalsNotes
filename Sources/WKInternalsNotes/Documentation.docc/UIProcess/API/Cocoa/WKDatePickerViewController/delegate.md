# ``WKInternalsNotes/WKDatePickerViewController/delegate``

`PUICQuickboardViewController` の delegate を使用する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <WKQuickboardViewControllerDelegate> delegate;
```

## Default Value
`initWithDelegate:` で設定される。

## Discussion
`@dynamic delegate` により実装はスーパークラスに委譲される。

## References
- [`WKDatePickerViewController.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.h#L35)
- [`WKDatePickerViewController.mm#L222`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L222)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
