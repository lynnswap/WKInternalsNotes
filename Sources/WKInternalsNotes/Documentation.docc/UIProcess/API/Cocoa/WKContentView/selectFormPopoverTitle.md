# ``WKInternalsNotes/WKContentView/selectFormPopoverTitle``

フォーム選択ポップオーバーのタイトルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *selectFormPopoverTitle;
```

## Default Value
`_inputPeripheral` が `WKFormSelectControl` でない場合は `nil`。

## Discussion
`_inputPeripheral` が `WKFormSelectControl` の場合は `selectFormPopoverTitle` を返す。

## References
- [`WKContentViewInteraction.h#L1062`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1062)
- [`WKContentViewInteraction.mm#L14536`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14536)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
