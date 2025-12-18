# ``WKInternalsNotes/WKView/_automaticallyAdjustsContentInsets``

コンテンツ inset を自動調整するか返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAutomaticallyAdjustsContentInsets:) BOOL _automaticallyAdjustsContentInsets;
```

## Default Value
`NO`。

## Discussion
getter は `NO` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L83)
- [`WKView.mm#L1345`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1345)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
