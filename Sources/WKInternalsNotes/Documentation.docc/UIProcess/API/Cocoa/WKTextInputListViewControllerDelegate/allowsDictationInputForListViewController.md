# ``WKInternalsNotes/WKTextInputListViewControllerDelegate/allowsDictationInputForListViewController(_:)``

音声入力の可否を返す。

## Objective-C Declaration
```objective-c
- (BOOL)allowsDictationInputForListViewController:(WKTextInputListViewController *)controller;
```

## Discussion
`supportsDictationInput` 内で参照される。

## References
- [`WKTextInputListViewController.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.h#L46)
- [`WKTextInputListViewController.mm#L160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L160)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
