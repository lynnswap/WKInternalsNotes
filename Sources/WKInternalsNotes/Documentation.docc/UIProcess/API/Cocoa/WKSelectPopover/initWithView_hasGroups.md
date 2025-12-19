# ``WKInternalsNotes/WKSelectPopover/initWithView(_:hasGroups:)``

select 用ポップオーバーを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithView:(WKContentView *)view hasGroups:(BOOL)hasGroups;
```

## Discussion
`WKSelectTableViewController` を生成して popover に関連付ける。タイトルがある場合は `UINavigationController` で包み、テーブルのサイズに合わせて `preferredContentSize` を設定する。最後に `UIPopoverController` を作成する。

## References
- [`WKFormSelectPopover.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPopover.h#L35)
- [`WKFormSelectPopover.mm#L380`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPopover.mm#L380)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
