# ``WKInternalsNotes/WKTextInputListViewController/delegate``

WKTextInputListViewController の delegate を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <WKTextInputListViewControllerDelegate> delegate;
```

## Default Value
未設定の場合は `nil`。

## Discussion
`@dynamic delegate` が指定されており、アクセサの実装はスーパークラス側に委ねられる。

## References
- [`WKTextInputListViewController.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.h#L60)
- [`WKTextInputListViewController.mm#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
