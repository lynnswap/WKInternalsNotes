# ``WKInternalsNotes/_WKTargetedElementInfo/hasAudibleMedia``

可聴メディアがあるかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL hasAudibleMedia;
```

## Default Value
`API::TargetedElementInfo::hasAudibleMedia()` の値。

## Discussion
内部の `_info` から `hasAudibleMedia()` を取得して返す。

## References
- [`_WKTargetedElementInfo.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L51)
- [`_WKTargetedElementInfo.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
