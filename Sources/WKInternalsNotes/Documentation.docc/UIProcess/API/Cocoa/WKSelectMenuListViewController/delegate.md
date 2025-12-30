# ``WKInternalsNotes/WKSelectMenuListViewController/delegate``

セレクトメニューの delegate を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <WKSelectMenuListViewControllerDelegate> delegate;
```

## Default Value
初期値は `nil`。

## Discussion
実装側では `@dynamic delegate` として扱い、ストレージは superclass に委譲する。

## References
- [`WKSelectMenuListViewController.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKSelectMenuListViewController.h#L46)
- [`WKSelectMenuListViewController.mm#L137`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKSelectMenuListViewController.mm#L137)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
