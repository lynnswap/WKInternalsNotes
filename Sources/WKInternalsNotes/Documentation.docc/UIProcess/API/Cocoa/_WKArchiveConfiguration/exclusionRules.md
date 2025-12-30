# ``WKInternalsNotes/_WKArchiveConfiguration/exclusionRules``

アーカイブ対象から除外するルールを保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSArray<_WKArchiveExclusionRule *> *exclusionRules;
```

## Default Value
初期値は `nil`。

## Discussion
自動合成プロパティで、`dealloc` で解放される。

## References
- [`_WKArchiveConfiguration.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKArchiveConfiguration.h#L36)
- [`_WKArchiveConfiguration.mm#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKArchiveConfiguration.mm#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
