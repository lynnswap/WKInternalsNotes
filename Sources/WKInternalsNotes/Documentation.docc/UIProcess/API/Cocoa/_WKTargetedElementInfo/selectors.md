# ``WKInternalsNotes/_WKTargetedElementInfo/selectors``

要素の selector を返す。shadow tree 内や未設定時は空配列。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<NSString *> *selectors;
```

## Default Value
`_info->selectors()` を条件付きで変換した配列。

## Discussion
selectors が空、または `_info->isInShadowTree()` が真なら `@[]` を返す。それ以外は `selectors().first()` を `NSArray<NSString *>` に変換して返す。

## References
- [`_WKTargetedElementInfo.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L54)
- [`_WKTargetedElementInfo.mm#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L85)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
