# ``WKInternalsNotes/_WKProcessInfo/physicalFootprint``

物理メモリフットプリント（bytes）を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) size_t physicalFootprint;
```

## Default Value
`initWithTaskInfo:` で `info.physicalFootprint` から設定される。

## Discussion
`TaskInfo` の physical footprint をそのまま保持して返す。

## References
- [`WKProcessPoolPrivate.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L60)
- [`WKProcessPool.mm#L745`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L745)
- [`WKProcessPool.mm#L771`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L771)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
