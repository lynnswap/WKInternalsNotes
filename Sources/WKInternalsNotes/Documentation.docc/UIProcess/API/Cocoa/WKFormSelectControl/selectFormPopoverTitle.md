# ``WKInternalsNotes/WKFormSelectControl/selectFormPopoverTitle``

ポップオーバー表示時のタイトルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *selectFormPopoverTitle;
```

## Discussion
`control` が `WKSelectPopover` の場合は `tableViewController.title` を返す。該当しない場合は `nil` を返す。

## References
- [`WKFormSelectControl.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.h#L45)
- [`WKFormSelectControl.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.mm#L109)
- [`WKFormSelectControl.mm#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.mm#L111)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
