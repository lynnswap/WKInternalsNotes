# ``WKInternalsNotes/_WKSerializedNode/new()``

`new` は `NS_UNAVAILABLE` で利用できない。

## Objective-C Declaration
```objective-c
+ (instancetype)new NS_UNAVAILABLE;
```

## Discussion
初期化子は公開されておらず、インスタンス生成は内部で行われる。

## References
- [`_WKSerializedNode.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSerializedNode.h#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
