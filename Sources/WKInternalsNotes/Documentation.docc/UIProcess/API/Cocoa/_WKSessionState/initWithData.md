# ``WKInternalsNotes/_WKSessionState/initWithData(_:)``

`NSData` から `SessionState` をデコードして初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithData:(NSData *)data;
```

## Discussion
`decodeSessionState` に失敗した場合は `self` を解放して `nil` を返す。

## References
- [`_WKSessionState.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSessionState.h#L33)
- [`_WKSessionState.mm#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSessionState.mm#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
