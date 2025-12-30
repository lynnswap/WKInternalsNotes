# ``WKInternalsNotes/_WKJSHandle/frame``

関連するフレーム情報を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) WKFrameInfo *frame;
```

## Default Value
`_ref->info().frameInfo` から生成された `WKFrameInfo`。

## Discussion
`FrameInfoData` を `API::FrameInfo` に変換して `WKFrameInfo` を返す。

## References
- [`_WKJSHandle.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKJSHandle.h#L39)
- [`_WKJSHandle.mm#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKJSHandle.mm#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
