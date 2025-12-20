# ``WKInternalsNotes/WKTextInputListViewController/initWithDelegate(_:)``

delegate を指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithDelegate:(id <WKTextInputListViewControllerDelegate>)delegate NS_DESIGNATED_INITIALIZER;
```

## Discussion
`[super initWithDelegate:dictationMode:]` を `PUICDictationModeText` で呼び出し、`_contextViewNeedsUpdate` を `YES` に設定する。`textInputContextForListViewController:` の結果を `textInputContext` に反映する。

## References
- [`WKTextInputListViewController.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.h#L54)
- [`WKTextInputListViewController.mm#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L42)
- [`WKTextInputListViewController.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
