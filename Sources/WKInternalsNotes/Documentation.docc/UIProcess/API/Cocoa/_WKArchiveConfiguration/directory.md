# ``WKInternalsNotes/_WKArchiveConfiguration/directory``

アーカイブ出力先のディレクトリを保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSURL *directory;
```

## Default Value
初期値は `nil`。

## Discussion
自動合成プロパティで、`dealloc` で解放される。

## References
- [`_WKArchiveConfiguration.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKArchiveConfiguration.h#L34)
- [`_WKArchiveConfiguration.mm#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKArchiveConfiguration.mm#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
