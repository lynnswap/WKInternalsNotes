# ``WKInternalsNotes/WKContentView/selectControl``

選択コントロールを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKFormSelectControl *selectControl;
```

## Default Value
`_inputPeripheral` が `WKFormSelectControl` の場合に返す。

## Discussion
`_inputPeripheral` が `WKFormSelectControl` のときにキャストして返し、それ以外は `nil`。

## References
- [`WKContentViewInteraction.h#L1067`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1067)
- [`WKContentViewInteraction.mm#L14436`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14436)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
