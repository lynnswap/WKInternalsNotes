# ``WKInternalsNotes/_WKInspectorWindow/forRemoteTarget``

リモートターゲット用ウィンドウかどうかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isForRemoteTarget) BOOL forRemoteTarget;
```

## Default Value
`NO`。

## Discussion
内部ヘッダで `readwrite` の `BOOL` として宣言されており、特別な実装はなく自動合成で保持される。

## References
- [`_WKInspectorWindow.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorWindow.h#L37)
- [`_WKInspectorWindowInternal.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorWindowInternal.h#L34)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
