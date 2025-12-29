# ``WKInternalsNotes/_WKInspectorExtension/delegate``

拡張のライフサイクルイベントを受け取る delegate。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <_WKInspectorExtensionDelegate> delegate WK_API_AVAILABLE(macos(12.0));
```

## Default Value
未設定時は `nil`。

## Discussion
getter は `_delegate` が保持する delegate を返す。setter は `delegate` が `nil` かつ `_delegate` が未設定なら何もしない。そうでなければ `InspectorExtensionDelegate` を作成して設定する。

## References
- [`_WKInspectorExtension.h#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.h#L101)
- [`_WKInspectorExtension.mm#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.mm#L63)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
