# ``WKInternalsNotes/WKSelectMenuListViewController/initWithDelegate(_:)``

セレクトメニュー用のビューコントローラを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithDelegate:(id <WKSelectMenuListViewControllerDelegate>)delegate NS_DESIGNATED_INITIALIZER;
```

## Discussion
`[super initWithDelegate:dictationMode:]` を `PUICDictationModeText` で呼び出す。

## References
- [`WKSelectMenuListViewController.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKSelectMenuListViewController.h#L46)
- [`WKSelectMenuListViewController.mm#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKSelectMenuListViewController.mm#L139)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
