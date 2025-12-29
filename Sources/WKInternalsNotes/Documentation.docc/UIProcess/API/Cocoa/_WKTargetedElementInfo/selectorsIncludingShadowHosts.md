# ``WKInternalsNotes/_WKTargetedElementInfo/selectorsIncludingShadowHosts``

shadow host を含む selector 群を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<NSArray<NSString *> *> *selectorsIncludingShadowHosts;
```

## Default Value
`_info->selectors()` を二重配列に変換した値。

## Discussion
`_info->selectors()` を走査し、各 selector を `NSString` に変換して `NSArray<NSArray<NSString *> *>` で返す。

## References
- [`_WKTargetedElementInfo.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L55)
- [`_WKTargetedElementInfo.mm#L96`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L96)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
