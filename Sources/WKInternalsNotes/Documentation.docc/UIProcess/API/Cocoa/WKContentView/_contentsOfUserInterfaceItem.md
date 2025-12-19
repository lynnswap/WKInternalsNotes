# ``WKInternalsNotes/WKContentView/_contentsOfUserInterfaceItem(_:)``

指定 UI アイテムの内容情報を返す。

## Objective-C Declaration
```objective-c
- (NSDictionary *)_contentsOfUserInterfaceItem:(NSString *)userInterfaceItem;
```

## Discussion
`actionSheet` や `contextMenu` などの識別子に応じて、現在利用可能な項目名や関連情報を辞書で返す。

## References
- [`WKContentViewInteraction.h#L1039`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1039)
- [`WKContentViewInteraction.mm#L14582`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14582)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
