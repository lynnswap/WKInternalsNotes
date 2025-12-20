# ``WKInternalsNotes/WKTextInputListViewController/reloadContextView()``

コンテキストビューの再読み込みを要求する。

## Objective-C Declaration
```objective-c
- (void)reloadContextView;
```

## Discussion
`_contextViewNeedsUpdate` を `YES` にして `reloadHeaderContentView` を呼び出す。

## References
- [`WKTextInputListViewController.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.h#L58)
- [`WKTextInputListViewController.mm#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L59)
- [`WKTextInputListViewController.mm#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L62)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
